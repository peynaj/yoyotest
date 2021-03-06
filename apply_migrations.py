from yoyo import read_migrations, get_backend
import settings

engine = 'postgres://{u}:{p}@{h}/{d}'.format(u=settings.USERNAME,
                                             p=settings.PASSWORD,
                                             h='localhost',
                                             d=settings.DBNAME
                                             )

backend = get_backend(engine)
migrations = read_migrations(settings.PROJECT_DIR + '/migrations')
print 'Count of migrations ---> {}'.format(len(migrations))
backend.apply_migrations(backend.to_apply(migrations))

