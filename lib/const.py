from os import path, makedirs

# ip 
PRIVATE_IP = '127.0.0.1' 
PUBLIC_IP = '127.0.0.1'

# ports 
FTP_PORT = 128
SSH_PORT = 256

# database 
DATABASE = 'lib/database.db'

# account
LOCK_TIME = 300 # in seconds
MAX_FAILED_ATTEMPTS = 3 # attempts before locking

if not path.exists('lib/cert'):
 makedirs('lib/cert')

CERT_FILE = 'lib/cert/public.crt'
KEY_FILE = 'lib/cert/private.key'
