import logging
import time

from datetime import timedelta
from flask import Blueprint, Response, request

from utils.config import POD_NAME
from utils.logging import is_ready_gauge, last_updated_gauge, job_start_counter, job_complete_counter, job_duration_summary
from write_xls import write_to_workbook, create_workbook

logger = logging.getLogger(__name__)
api_endpoints = Blueprint('api', __name__, url_prefix='/api')

# NB: uncomment code in main.py to enable these endpoints
# Any endpoints added here will be available at /api/<endpoint> - e.g. http://127.0.0.1:8080/api/example
# Change the the example below to suit your needs + add more as needed

# Set initial metrics
is_ready_gauge.labels(error_type=None, job_name=POD_NAME).set(1)
last_updated_gauge.set_to_current_time()


@api_endpoints.route('/export', methods=['GET', 'POST'])
def export():
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            payload = request.get_json()

            # Set metrics for the job
            logger.info('Started job writexls')
            job_start_counter.labels(job_name='writexls').inc()

            # Do job
            print('Performing job writexls')
            file_data = write_to_workbook(create_workbook(), payload)

            # Set metrics after completing job
            logger.info('Completed job writexls')
            start_time = time.time()
            duration = timedelta(seconds=(time.time() - start_time))

            job_duration_summary.labels(job_name='writexls', status='success').observe(duration.total_seconds())
            job_complete_counter.labels(job_name='writexls', status='success').inc()

            return Response({'content': file_data}, status=200)
        else:
            return Response('Content-Type must be application/json', status=400)
    else:
        return Response('Method must be POST', status=400)
