import psycopg2

username = 'Bilovodskiy_I'
password = '1234'
database = 'laptops'
host = 'localhost'
port = '5432'

query_1 = '''
select gpu_series,count(name) from laptop 
inner join gpu on laptop.gpu_id=gpu.gpu_id 
group by gpu_series	
'''
query_2 = '''
select cpu_series,count(name) from laptop 
inner join cpu on laptop.cpu_id=cpu.cpu_id 
group by cpu_series

'''

query_3 = '''
select os_name,count(name) from laptop 
inner join os on laptop.os_id=os.os_id 
group by os_name
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    print('Query 1:')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\nQuery 2:')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\nQuery 3:')
    cur.execute(query_3)
    for row in cur:
        print(row)