from yoyo import read_migrations, get_backend
import settings

engine = 'postgres://{u}:{p}@{h}/{d}'.format(u=settings.USERNAME,
                                             p=settings.PASSWORD,
                                             h='localhost',
                                             d=settings.DBNAME
                                             )

backend = get_backend(engine)
migrations = read_migrations(settings.PROJECT_DIR + '/migrations')
print '----> {}'.format(len(migrations))
backend.rollback_migrations(backend.to_apply(migrations))

