from yoyo import read_migrations, get_backend
# from .settings import PROJECT_DIR

backend = get_backend('postgres://peymandb:123456@localhost/peymandb')
migrations = read_migrations('/home/peyman/Projects/yoyotest/migrations')
print '----> {}'.format(len(migrations))
backend.rollback_migrations(backend.to_apply(migrations))

