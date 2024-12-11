def count_failed_logins(logs):
    return sum(1 for log in logs if "failure" in log)

def list_failed_ips(logs):
    return list(set(log.split(":")[0] for log in logs if "failure" in log))
