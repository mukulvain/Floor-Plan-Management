from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])
def log(index_name, data):
    try:
        es.index(index=index_name, body=data)
        print("Data logged successfully to Elasticsearch!")
    except Exception as e:
        print(f"Failed to log data to Elasticsearch: {str(e)}")

log_index = "log"
log_entry = {
    "timestamp": "2023-12-01T12:00:00",
    "message": "This is a log message.",
    "level": "INFO",
    "source": "Application"
}
log(log_index, log_entry)
