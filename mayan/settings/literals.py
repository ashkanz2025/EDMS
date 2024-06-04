BINARY_DOCKER_COMPOSE_VERSION = '1.29.2'
DEFAULT_DIRECTORY_BASE = '/opt/'
DEFAULT_DIRECTORY_INSTALLATION = '/opt/mayan-edms/'
DEFAULT_DIRECTORY_MEDIA_ROOT = '/opt/mayan-edms/media/'
DEFAULT_DATABASE_NAME = 'mayan'
DEFAULT_DATABASE_PASSWORD = 'mayandbpass'
DEFAULT_DATABASE_USER = 'mayan'
DEFAULT_ELASTICSEARCH_PASSWORD = 'mayanespassword'
DEFAULT_KEYCLOAK_ADMIN = 'admin'
DEFAULT_KEYCLOAK_ADMIN_PASSWORD = 'admin'
DEFAULT_KEYCLOAK_DATABASE_HOST = 'keycloak-postgres'
DEFAULT_KEYCLOAK_DATABASE_NAME = 'keycloak'
DEFAULT_KEYCLOAK_DATABASE_PASSWORD = 'keycloakdbpass'
DEFAULT_KEYCLOAK_DATABASE_USERNAME = 'keycloak'
DEFAULT_OS_DISTRIBUTION = '"Debian 12"'
DEFAULT_OS_GROUP = 'mayan'
DEFAULT_OS_USERNAME = 'mayan'
DEFAULT_RABBITMQ_PASSWORD = 'mayanrabbitpass'
DEFAULT_RABBITMQ_USER = 'mayan'
DEFAULT_RABBITMQ_VHOST = 'mayan'
DEFAULT_REDIS_PASSWORD = 'mayanredispassword'
DEFAULT_SECRET_KEY = 'secret-key-missing!'
DEFAULT_USER_SETTINGS_FOLDER = 'user_settings/'
DEFAULT_USER_SETTINGS_MODULE = 'user_settings'
DJANGO_SERIES = '4.2'
DOCKER_HOST_REGISTRY_NAME = 'docker-registry.local'
DOCKER_HOST_REGISTRY_PORT = 5000
DOCKER_IMAGE_MAYAN_NAME = 'mayanedms/mayanedms'
DOCKER_IMAGE_MAYAN_TAG = 's4.7'
DOCKER_DIND_IMAGE_VERSION = 'docker:23.0.6-dind'
DOCKER_ELASTIC_IMAGE_NAME = 'elasticsearch'
DOCKER_ELASTIC_IMAGE_TAG = '7.17.20'
DOCKER_KEYCLOAK_IMAGE_NAME = 'keycloak/keycloak'
DOCKER_KEYCLOAK_IMAGE_TAG = '20.0.5-0'
DOCKER_KEYCLOAK_POSTGRES_IMAGE_NAME = 'postgres'
DOCKER_KEYCLOAK_POSTGRES_IMAGE_TAG = '13.15-alpine'
DOCKER_LINUX_IMAGE_VERSION = 'debian:12.5-slim'
DOCKER_MYSQL_IMAGE_VERSION = 'mysql:8.0.36'
DOCKER_ORACLE_IMAGE_VERSION = 'wnameless/oracle-xe-11g-r2'
DOCKER_POSTGRESQL_IMAGE_NAME = 'postgres'
DOCKER_POSTGRESQL_IMAGE_TAG = '14.12-alpine'
DOCKER_POSTGRESQL_MAX_CONNECTIONS = 150
DOCKER_PYTHON_IMAGE_VERSION = 'python:3.11.9-slim'
DOCKER_RABBITMQ_IMAGE_NAME = 'rabbitmq'
DOCKER_RABBITMQ_IMAGE_TAG = '3.12.28-management-alpine'
DOCKER_REDIS_IMAGE_NAME = 'redis'
DOCKER_REDIS_IMAGE_TAG = '7.0.15-alpine'
DOCKER_TRAEFIK_IMAGE_NAME = 'traefik'
DOCKER_TRAEFIK_IMAGE_TAG = 'v2.5.7'
GIT_REMOTE_NAME = 'origin'
GITLAB_CI_BRANCH_BUILDS_DOCKER = 'builds/docker'
GITLAB_CI_BRANCH_BUILDS_DOCUMENTATION = 'builds/documentation'
GITLAB_CI_BRANCH_BUILDS_PYTHON = 'builds/python'
GITLAB_CI_BRANCH_DEPLOYMENTS_DEMO = 'deployments/demo'
GITLAB_CI_BRANCH_DEPLOYMENTS_STAGING = 'deployments/staging'
GITLAB_CI_BRANCH_RELEASES_ALL_MAJOR = 'releases/all/major'
GITLAB_CI_BRANCH_RELEASES_ALL_MINOR = 'releases/all/minor'
GITLAB_CI_BRANCH_RELEASES_DOCKER_MAJOR = 'releases/docker/major'
GITLAB_CI_BRANCH_RELEASES_DOCKER_MINOR = 'releases/docker/minor'
GITLAB_CI_BRANCH_RELEASES_DOCUMENTATION = 'releases/documentation'
GITLAB_CI_BRANCH_RELEASES_NIGHTLY = 'releases/nightly'
GITLAB_CI_BRANCH_RELEASES_PYTHON_MAJOR = 'releases/python/major'
GITLAB_CI_BRANCH_RELEASES_PYTHON_MINOR = 'releases/python/minor'
GITLAB_CI_BRANCH_RELEASES_STAGING = 'releases/staging'
GITLAB_CI_BRANCH_RELEASES_TESTING = 'releases/testing'
GITLAB_CI_BRANCH_TESTS_ALL = 'tests/all'
GITLAB_CI_BRANCH_TESTS_DOCKER = 'tests/docker'
GITLAB_CI_BRANCH_TESTS_PYTHON_ALL = 'tests/python/all'
GITLAB_CI_BRANCH_TESTS_PYTHON_BASE = 'tests/python/base'
GITLAB_CI_BRANCH_TESTS_PYTHON_UPGRADE = 'tests/python/upgrade'
GUNICORN_LIMIT_REQUEST_LINE = 4094
GUNICORN_MAX_REQUESTS = 500
GUNICORN_REQUESTS_JITTER = 50
GUNICORN_TIMEOUT = 120
GUNICORN_WORKER_CLASS = 'gevent'
GUNICORN_WORKERS = 3
LOCAL_VERSION = ''
PYTHON_AMQP_VERSION = '5.2.0'
PYTHON_MYSQL_VERSION = '2.0.3'
PYTHON_ORACLE_VERSION = '8.1.0'
PYTHON_PIP_VERSION = '24.0'
PYTHON_PSYCOPG_VERSION = '3.1.14'
PYTHON_PSYCOPG_VERSION_PREVIOUS = '2.9.9'
PYTHON_PSUTIL_VERSION = '5.8.0'
PYTHON_REDIS_VERSION = '5.0.3'
PYTHON_WHEEL_VERSION = '0.43.0'
SOURCE_CODE_REPOSITORY = 'https://gitlab.com/mayan-edms/mayan-edms/'
SOURCE_CODE_GIT = 'https://gitlab.com/mayan-edms/mayan-edms.git'
SOURCE_CODE_ISSUES = 'https://gitlab.com/mayan-edms/mayan-edms/issues/'
SECRET_KEY_FILENAME = 'SECRET_KEY'
SYSTEM_DIR = 'system'
SUPERVISOR_CONFIGURATION_DIRECTORY = '/etc/supervisor/conf.d/'
SUPERVISOR_CONFIGURATION_FILENAME = 'mayan-edms.conf'
MAYAN_WORKER_A_CONCURRENCY = 0
MAYAN_WORKER_A_MAX_MEMORY_PER_CHILD = 400000
MAYAN_WORKER_A_MAX_TASKS_PER_CHILD = 1000
MAYAN_WORKER_A_NICE_LEVEL = 0
MAYAN_WORKER_B_CONCURRENCY = 0
MAYAN_WORKER_B_MAX_MEMORY_PER_CHILD = 400000
MAYAN_WORKER_B_MAX_TASKS_PER_CHILD = 1000
MAYAN_WORKER_B_NICE_LEVEL = 2
MAYAN_WORKER_C_CONCURRENCY = 0
MAYAN_WORKER_C_MAX_MEMORY_PER_CHILD = 400000
MAYAN_WORKER_C_MAX_TASKS_PER_CHILD = 1000
MAYAN_WORKER_C_NICE_LEVEL = 10
MAYAN_WORKER_D_CONCURRENCY = 1
MAYAN_WORKER_D_MAX_MEMORY_PER_CHILD = 400000
MAYAN_WORKER_D_MAX_TASKS_PER_CHILD = 100
MAYAN_WORKER_D_NICE_LEVEL = 15
MAYAN_WORKER_E_CONCURRENCY = 0
MAYAN_WORKER_E_MAX_MEMORY_PER_CHILD = 400000
MAYAN_WORKER_E_MAX_TASKS_PER_CHILD = 1000
MAYAN_WORKER_E_NICE_LEVEL = 2
