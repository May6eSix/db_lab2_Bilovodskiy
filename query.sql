 
select gpu_series,count(name) from laptop 
	inner join gpu on laptop.gpu_id=gpu.gpu_id 
	group by gpu_series
	
	
	
select cpu_series,count(name) from laptop 
	inner join cpu on laptop.cpu_id=cpu.cpu_id 
	group by cpu_series


select os_name,count(name) from laptop 
	inner join os on laptop.os_id=os.os_id 
	group by os_name
