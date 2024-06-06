### 1. Telegraf Setup:
- Install [Telegraf](https://docs.influxdata.com/telegraf/v1/install/) on Linux VMs. Telegraf has built-in plugins for collecting CPU, memory, disk, and other system metrics.
- Configure Telegraf to scrape metrics at regular intervals (e.g., every 10 seconds) and send them to desired output (e.g., [InfluxDB](https://docs.influxdata.com/influxdb/v2/install/?t=Linux) or [Prometheus](https://prometheus.io/docs/prometheus/latest/installation/)).
### 2. Metrics Collection:
#### Telegraf provides various input plugins:
- **CPU Metrics:** Collect CPU usage (user, system, idle, etc.).
- **Memory Metrics:** Gather memory utilization (used, free, cached, etc.).
- **Disk Metrics:** Monitor disk space (used, available, I/O rates).

#### Application Logs:
For application logs, consider using rsyslog or syslog-ng to centralize logs.
- Configure applications to log to a common location (e.g., /var/log/appname.log).
- Telegraf also has an exec input plugin that can execute custom scripts to collect logs - [Exec & Execd.](https://www.influxdata.com/blog/plugin-spotlight-exec-execd/)
### 3. Structured Dataset Creation:
- Combine metric data (CPU, memory, disk) and logs into a single dataset.
- Each row represents a timestamp, and columns include metrics (CPU usage, memory utilization, disk space) and apllication log features (e.g. error counts, warnings).
- Additional features could include:
  - Timestamp: Encode timestamps as features (hour, minute, day of the week).
  - Metric Averages: Calculate moving averages for metrics.
  - Anomalies: Detect anomalies using statistical methods.[1]

### 4. Labeling:
- Define target variable (label). For example, if the predicting system failure, label it as 1 when a failure occurs and 0 otherwise.
- Align timestamps between metrics and logs to create labeled examples.
### 5. Feature Selection:
- Relevant features:
  - Raw metrics (CPU, memory, disk).
  - Derived features (averages, percentiles).
  - Time-related features.
  - Log-based features (error counts, log levels).
- Avoid irrelevant features that don’t contribute to prediction. [2]

### Reference:
1. https://towardsdatascience.com/statistical-techniques-for-anomaly-detection-6ac89e32d17a 

2. https://machinelearningmastery.com/an-introduction-to-feature-selection/
