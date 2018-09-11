def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('merge_paths', '/merge_paths')
    config.add_route('save_points', '/save_points')
