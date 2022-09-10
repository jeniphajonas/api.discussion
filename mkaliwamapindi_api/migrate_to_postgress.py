import sys
import mysql.connector
import psycopg2
import progressbar

# Mysql connection
try:
    cnx_msql = mysql.connector.connect(
        host="localhost", user="root", passwd="", db="mkaliwamapindi")
except mysql.connector.Error as e:
    print("MYSQL: Unable to connect!"), e.msg
    sys.exit(1)


# Postgresql connection
try:
    cnx_psql = psycopg2.connect(
        "postgresql://postgres:admin@localhost/mkaliwamapindi")
except psycopg2.Error as e:
    print('PSQL: Unable to connect!\n{0}').format(e)
    sys.exit(1)


# Cursors initializations
cur_msql = cnx_msql.cursor(buffered=True, dictionary=True)
cur_psql = cnx_psql.cursor()


def select_and_insert(mysql_query, psql_query):
    cur_msql.execute(mysql_query)
    count = 0
    bar = progress_bar(cur_msql.rowcount)

    for row in cur_msql:
        try:
            cur_psql.execute(psql_query, row)
            count += 1
            bar.update(count)
        except psycopg2.Error as e:
            sys.exit(str(e))


def progress_bar(count):
    widgets = [' [',
               progressbar.Timer(format='elapsed time: %(elapsed)s'),
               '] ',
               progressbar.Bar('*'), ' (',
               progressbar.ETA(), ') ',
               ]
    bar = progressbar.ProgressBar(
        max_value=count, widgets=widgets).start()
    return bar


  # Example of migrating mapindi
def migrate_mapindi():
    msql_q = "SELECT id, user_id, season_id, winner_status,vote, first_name, last_name, school_name,school_location,subject_name,class_name,lesson,description,video_id,date_uploaded,status FROM mapindi"

    psql = "INSERT INTO mapindi (id, user_id,season_id, winner_status, vote, first_name, last_name, school_name,school_location,subject_name,class_name,lesson,description,video_id,date_uploaded,status)\
            VALUES (%(id)s, %(user_id)s, %(season_id)s, %(winner_status)s, %(vote)s,  %(first_name)s, %(last_name)s, %(school_name)s,%(school_location)s,%(subject_name)s,%(class_name)s,%(lesson)s,%(description)s,%(video_id)s,%(date_uploaded)s,%(status)s)"

    return select_and_insert(msql_q, psql)

if __name__ == "__main__":
    migrate_mapindi()

# Closing cursors
cur_msql.close()
cur_psql.close()

# Committing
cnx_psql.commit()

# Closing database connections
cnx_msql.close()
cnx_psql.close()


