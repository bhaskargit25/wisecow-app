import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # in percent
MEMORY_THRESHOLD = 80.0  # in percent
DISK_THRESHOLD = 80.0  # in percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    else:
        logging.info(f'CPU usage is normal: {cpu_usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
    else:
        logging.info(f'Memory usage is normal: {memory_usage}%')

def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk space usage detected: {disk_usage}%')
    else:
        logging.info(f'Disk space usage is normal: {disk_usage}%')

def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'username'])]
    logging.info(f'Running processes: {processes}')

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()

if __name__ == "__main__":
    main()
