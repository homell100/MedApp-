import psycopg2 as pg2
import config as cfg

def make_connection():
	conn = pg2.connect(database=cfg.DB,
						 user=cfg.USER,
						 password=cfg.PASSWORD)
						
	return conn