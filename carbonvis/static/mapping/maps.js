// Class Definitions
class Point {
    constructor(id, lat, long, recorded) {
      this.id = id;
      this.lat = lat;
      this.long = long;
      this.recorded = recorded;
    }

    latlong(){
      return {lat: this.lat, lng: this.long};
    }
}

class EmissionsController{
    constructor() {
      this.vehicles = {};
    }

    add_vehicle(type, title, emissions){
      this.vehicles[type] = {'title': title, 'emissions': emissions}
    }

    get_vehicles(){
      return this.vehicles;
    }

    get_emissions(type){
      return this.vehicles[type]['emissions'];
    }

    get_vehicle_series(distance, selected_type){
      var data = [];
      var sorted_vehicles = _.sortBy(this.vehicles, ['emissions', 'title']);
      var selected_index = 0;
      for (var type in sorted_vehicles) {
        if(sorted_vehicles[type]['title']===this.vehicles[selected_type]['title']){
            selected_index = type;
        }
        data.push([
         sorted_vehicles[type]['title'],
          Number.parseFloat(distance * sorted_vehicles[type]['emissions'])
        ])
      }
      selected_index = Number.parseInt(selected_index);
      var series = [{
                name: 'CO₂-Verbrauch',
                data: data,
                zoneAxis: 'x',
                zones: [
                    {value: selected_index},
                    {value: selected_index+1, color: '#00FF00'},
                ],
                dataLabels: {
                  enabled: true,
                  rotation: -90,
                  allowOverlap: true,
                  color: '#666666',
                  align: 'left',
                  format: '{point.y:.1f} g', // one decimal
                  y: -10, // 10 pixels down from the top
                  style: {
                      fontSize: '10px',
                      fontFamily: 'Raleway, sans-serif'
                  }
              }
      }]
      return series
    }

    get_form(path_id, selected_type){
      var form_html = `
      <form>
      <select id='vehicle_select_${path_id}' data-path-id='${path_id}'>`;
      for (var type in this.vehicles) {
        var selected = "";
        if(selected_type === type){
          selected = " selected";
        }
        form_html += `<option value="${type}" ${selected}>${this.vehicles[type]['title']}</option>`;
      }
      form_html += `</select></form>`;
      return form_html;
    }

    get_scaled_width(type){
      return this.vehicles[type]['emissions'] * (50 - 5)/(100 - 1) + 5
    };

    interpolate_gradient(type) {

      var a = "#44FF00",
          b = "#FF0000",
          amount = this.vehicles[type]['emissions'] * 1 / (400 - 1),
          ah = parseInt(a.replace(/#/g, ''), 16),
          ar = ah >> 16, ag = ah >> 8 & 0xff, ab = ah & 0xff,
          bh = parseInt(b.replace(/#/g, ''), 16),
          br = bh >> 16, bg = bh >> 8 & 0xff, bb = bh & 0xff,
          rr = ar + amount * (br - ar),
          rg = ag + amount * (bg - ag),
          rb = ab + amount * (bb - ab);

    return '#' + ((1 << 24) + (rr << 16) + (rg << 8) + rb | 0).toString(16).slice(1);
};

    //
}

class DisplayController{
    constructor(map) {
      this.map = map;
      this.current_marker = null;
    }

    show_info(marker){
      if(this.current_marker != null){
        this.current_marker.info.close();
      }
      this.current_marker = marker;
      this.current_marker.info.open(
        this.map, this.current_marker);
    }
}

class Path {
    constructor(id, points, duration, footprint, distance, map, display, emissions) {
        this.map = map
        this.id = id;
        this.points = points;
        this.duration = duration;
        this.footprint = footprint;
        this.distance = distance;

        this.display = display;
        this.shown = false;
        this.edit = false;
        this.emissions = emissions;

        this.vehicle = "ucarver";

        this.init();
    }

    drawPolyline(){

      this.polyline = null;
      this.polyline_emissions = null;

      var points_latlong = []
      for (var i = 0; i < this.points.length; i++) {
        points_latlong.push(this.points[i].latlong())
      }

      this.polyline = new google.maps.Polyline({
          path: points_latlong,
          geodesic: true,
          strokeColor: '#1391B4',
          strokeOpacity: 1,
          zindex: 5,
          strokeWeight: 3
      });

      this.polyline_emissions = new google.maps.Polyline({
          path: points_latlong,
          geodesic: true,
          // strokeColor: '#1391B4',
          strokeColor: emissions.interpolate_gradient(this.vehicle),
          strokeOpacity: 0.3,
          zindex: 1,
          strokeWeight: this.emissions.get_scaled_width(this.vehicle)
      });

      // Events
      this.polyline.path = this;
      this.polyline_emissions.path = this;

      google.maps.event.addListener(this.polyline, 'click', function() {
          this.path.show_info_window(true);
      });
      google.maps.event.addListener(this.polyline_emissions, 'click', function() {
          this.path.show_info_window(true);
      });
      google.maps.event.addListener(this.polyline, 'mouseover', function() {
          this.path.show_info_window();
      });
      google.maps.event.addListener(this.polyline, 'mouseout', function() {
          this.path.hide_info_window();
      });

      google.maps.event.addListener(this.polyline_emissions, 'mouseover', function() {
          this.path.show_info_window();
      });
      google.maps.event.addListener(this.polyline_emissions, 'mouseout', function() {
          this.path.hide_info_window();
      });

    };

    drawEditMarkers(){
      this.editMarkers = [];

      for (var i = 0; i < this.points.length; i++) {
        var pm = new google.maps.Marker({
            position: this.points[i].latlong(),
            map: null,
            draggable: true
        });
        this.bindMarkerToPolylines(pm, i);
        this.editMarkers.push(pm)
      }
    };

    drawMarkers(){

      this.markers = [];

      var s_info = new google.maps.InfoWindow({
          content: `<h4>Start</h4><br /><b>Uhrzeit:</b> ${this.points[this.points.length - 1].recorded}`
      });
      var s_marker = new mapIcons.Marker({
          position: this.points[0].latlong(),
          map: null,
          title: `Start @ {this.points[0].recorded}`,
          icon: {
              path: mapIcons.shapes['MAP_PIN'],
              fillColor: '#12AEAD',
              fillOpacity: 0.8,
              strokeColor: '#FFFFFF',
              strokeWeight: 0
          },
          map_icon_label: '<span class="map-icon map-icon-skateboarding"></span>',
      });
      s_marker.info = s_info;
      s_marker.display = this.display;

      google.maps.event.addListener(s_marker, 'click', function() {
          this.display.show_info(s_marker);
      });

      this.markers.push(s_marker);

      var e_info = new google.maps.InfoWindow({
          content: `
            <h4>Ende</h4><br />
            <b>Uhrzeit:</b> ${this.points[this.points.length - 1].recorded}<br />`
      });
      var e_marker = new mapIcons.Marker({
          position: this.points[this.points.length - 1].latlong(),
          map: null,
          title: 'Ende',
          icon: {
              path: mapIcons.shapes['MAP_PIN'],
              fillColor: '#DB524F',
              fillOpacity: 0.8,
              strokeColor: '#FFFFFF',
              strokeWeight: 0,
              size: new google.maps.Size(2, 3),
          },
          map_icon_label: '<span class="map-icon map-icon-skateboarding"></span>',
      });
      e_marker.info = e_info;
      e_marker.display = this.display;
      var path_id = this.id;
      google.maps.event.addListener(e_marker, 'click', function() {
          this.display.show_info(e_marker);
      });
      this.markers.push(e_marker);

      // for (var i = 0; i < this.points.length; i++) {
      //     var marker = new mapIcons.Marker({
      //         position: this.points[i].latlong(),
      //         map: null,
      //         title: '',
      //         icon: {
      //             path: google.maps.SymbolPath.CIRCLE,
      //             scale: 2
      //         }
      //     });
      //     this.markers.push(marker);
      // }
    }

    init(){
      this.drawPolyline();
      this.drawMarkers();
      this.drawEditMarkers();
      this.hideEditMarkers();
    };

    clear(){
      this.hide();
      this.polyline = null;
      this.polyline_emissions = null;
      this.markers = [];
      this.editMarkers = [];
    };

    redraw(){
      this.clear();
      this.drawPolyline();
      this.drawEditMarkers();
      this.show(false);
      this.showEditMarkers();
    }

    show(center=true) {
        this.polyline.setMap(this.map);
        this.polyline_emissions.setMap(this.map);
        this.showMarkers();
        this.shown = true;
        this.get_checkbox().prop("checked", true);
        this.get_edit_link().css("display", '');
        this.get_info_link().css("display", '');
        if(center) this.center_map();
    }

    hide_info_window(){
      if($('#info_window')[0].dataset['sticky']==='true') return;

      hideInfoWindow();
    }

    show_info_window(sticky=false){
      if($('#info_window')[0].dataset['sticky']==='true' && sticky===false) return;
      var style_display = "none";
      if(sticky===true){
         $('#info_window')[0].dataset['sticky'] = true;
         style_display = "";
      }
      var info_content = `
          <a href="#" class="close_button" onclick="hideInfoWindow()" style="display: ${style_display};"></a>
          <h3><span class="smaller">Trip ${this.id}</span>
          </h3>
          <div id='info_content'>
            <b>Uhrzeit:</b>${this.points[this.points.length - 1].recorded} - ${this.points[this.points.length - 1].recorded}<br />
            <b>Fahrzeit:</b> ${this.duration}<br />
            <b>Distanz:</b> ${this.distance} km<br />
            <b>CO₂-Fussabdruck:</b> ${this.get_emissions(this.vehicle)} g CO&#8322;<br /><br />
            <b>Fahrzeugtyp:</b><br /> ${this.emissions.get_form(this.id, this.vehicle)}<br /><br />
            <div id="chart" style="min-width: 350px; height: 600px; margin: 0 auto"></div>
            </div>
      `
      $('#info_window').css("display", "block");
      $('#info_window').html(info_content);

      $(`#vehicle_select_${this.id}`).change(function(){
              setPathVehicle(this.dataset['pathId'], $(this).val())
      });


      this.info_chart = Highcharts.chart('chart', {
          chart: {
              type: 'column'
          },
          title: {
              text: 'CO₂-Fussabdruck-Vergleich'
          },
          subtitle: {
              text: ''
          },
          xAxis: {
              type: 'category',
              labels: {
                  rotation: -90,
                  style: {
                      fontSize: '13px',
                      fontFamily: 'Verdana, sans-serif'
                  }
              }
          },
          yAxis: {
              min: 0,
              title: {
                  text: 'CO₂-Verbrauch'
              }
          },
          legend: {
              enabled: false
          },
          tooltip: {
              pointFormat: 'CO₂: <b>{point.y:.1f} g </b>'
          },
          series: this.emissions.get_vehicle_series(this.distance, this.vehicle),
      });
    }

    center_map(){
      var bounds = new google.maps.LatLngBounds();
      this.polyline.getPath().forEach(function(latLng) {
        bounds.extend(latLng);
      });
      this.map.fitBounds(bounds);
    }

    showMarkers() {
        for (var i = 0; i < this.markers.length; i++) {
            this.markers[i].setMap(this.map);
        }
    }

    showEditMarkers() {
        for (var i = 0; i < this.editMarkers.length; i++) {
            this.editMarkers[i].setMap(this.map);
        }
    }

    toggle() {
        if(this.shown) this.hide();
        else this.show();
    }

    savePoints(){
        $.post("save_points", { points_json:JSON.stringify(this.points) });
    }

    toggleEdit(){
      if(this.edit) {
        this.hideEditMarkers();
        this.clear();
        this.drawPolyline();
        this.drawMarkers();
        this.show();
        this.get_edit_link().text('Anpassen');
        this.edit = false;

        this.savePoints();
      }
      else{
        this.hideMarkers();
        this.clear();
        this.drawPolyline();
        this.drawEditMarkers();
        this.show();
        this.showEditMarkers();
        this.get_edit_link().text('Speichern');
        this.edit = true;
      }
    }

    hide() {
        this.hideMarkers();
        this.hideEditMarkers();

        this.polyline.setMap(null);
        this.polyline_emissions.setMap(null);
        this.shown = false;
        this.get_checkbox().prop("checked", false);

        this.get_edit_link().css("display", 'None');
        this.get_info_link().css("display", 'None');
    }

    hideMarkers() {
        for (var i = 0; i < this.markers.length; i++) {
            this.markers[i].setMap(null);
        }
    }

    hideEditMarkers(){
      for (var i = 0; i < this.editMarkers.length; i++) {
            this.editMarkers[i].setMap(null);
      }
    }

    get_checkbox() {
      var checkbox_id = "#path_" + this.id;
      return $(checkbox_id);
    }

    get_edit_link(){
      var link_id = "#editPathLink_" + this.id;
      return $(link_id);
    }

    get_info_link(){
      var link_id = "#showPathInfo_" + this.id;
      return $(link_id);
    }

    //getter
    get get_path_length() {
      return google.maps.geometry.spherical.computeLength(this.polyline.getPath().getArray()) / 1000
    }

    get_center_point(){
      return this.points[Math.floor(this.points.length / 2)];
    }

    get_center(){
      var center_point = this.get_center_point()
      return {lat: center_point.lat, lng: center_point.long}
    }

    get_emissions(vehicle){
      return Number.parseFloat(this.distance * this.emissions.get_emissions(vehicle)).toFixed(2);
    }

    bindMarkerToPolylines(marker, index) {
      var the_path = this;
      var points = this.points;
      google.maps.event.addListener(marker, 'dragend', function() {
          var nextlatlng, prevlatlng, newMarkerLatLng = marker.getPosition();

          // update our lat/lng values
          points[index].lat = newMarkerLatLng.lat();
          points[index].long = newMarkerLatLng.lng();
          the_path.redraw();
      });
    }

};

class PathController{
    constructor() {
        this.paths = [];
    }

    push(path){
      this.paths[path.id] = path
    }

    show(path_id) {
        this.paths[path_id].show();
    }

    get(path_id) {
       return this.paths[path_id];
    }

    hide(path_id) {
        this.paths[path_id].hide();
    }

    toggleEdit(path_id){
      this.paths[path_id].toggleEdit();
    }

    toggle(path_id) {
        this.paths[path_id].toggle();
    }

    clearAllPaths() {
      for (var path_id in this.paths) {
        this.paths[path_id].hide();
      }
    }

    showAllPaths() {
      for (var path_id in this.paths) {
        this.paths[path_id].show();
      }
    }

    setVehicle(path_id, vehicle){
      this.paths[path_id].vehicle = vehicle;
      this.paths[path_id].clear();
      this.paths[path_id].init();
      this.paths[path_id].show();
      this.paths[path_id].show_info_window(true);
    }
};

function show_path(path_id) {
    paths.show(path_id)
};

function showInfoWindow(path_id) {
    paths.get(path_id).show_info_window(true);
};


function toggle_path(path_id) {
    paths.toggle(path_id)
};

function clearPaths() {
    paths.clearAllPaths();
};

function showPaths() {
    paths.showAllPaths();
};

function nextPath() {
    paths.show_next();
};

function prevPath() {
    paths.show_prev();
};

function toggleEditPath(path_id){
  paths.toggleEdit(path_id);
};

function setPathVehicle(path_id, vehicle){
  paths.setVehicle(path_id, vehicle);
};

function hideInfoWindow(){
  $('#info_window').css("display", 'none');
  $('#info_window')[0].dataset['sticky'] = false;
}

function mergePaths(){
  var path_ids = [];
  var vehicle_id = $('#datastore').data('vehicleId');
  $('.pathCheck:checkbox:checked').each(function(){
    path_ids.push($( this ).data('pathId'));
  });
  target_url = "merge_paths?vehicle_id=" + vehicle_id + "&path_ids=" + path_ids.join();
  console.log(target_url);
  window.location.href=target_url;
};
