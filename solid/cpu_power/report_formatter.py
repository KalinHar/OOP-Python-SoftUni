from datetime import timedelta


def format_report(report):
    return '\n'.join([time.strftime('%H:%M:%S:%f') + " " + str(measurement)
                      for time, measurement in report])
