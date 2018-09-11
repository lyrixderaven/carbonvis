import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from carbonvis.models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from carbonvis.models import Path
from carbonvis.models import Point
from carbonvis.models import Vehicle

from sqlalchemy import MetaData


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) < 1:
        usage(argv)
    config_uri = argv[1]

    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = get_engine(settings)

    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        models = [Point, Path]
        for m in models:
            for m in dbsession.query(m).all():
                dbsession.delete(m)
            transaction.commit()

    print(dbsession.query(Point).count())
    print(dbsession.query(Path).count())
    print(dbsession.query(Vehicle).count())



