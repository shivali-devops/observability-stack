# observability-stack

A hands-on observability stack featuring Prometheus, Grafana, Alertmanager, and Node Exporter. Includes real-world monitoring setups, alerting rules, Slack notifications, and Docker-based labs for DevOps practice.

## 📋 Overview

This project demonstrates a complete monitoring and alerting infrastructure using industry-standard tools. It includes:

- **Prometheus**: Metrics collection and storage
- **Grafana**: Visualization and dashboarding
- **Alertmanager**: Alert routing and notifications
- **Node Exporter**: System metrics collection
- **Custom Flask App**: Demo application with Prometheus metrics

## 🏗️ Architecture

```
┌─────────────────┐
│   Node Exporter │──┐
└─────────────────┘  │
                     │
┌─────────────────┐  │      ┌──────────────┐      ┌─────────────┐
│   App Demo      │──┼─────►│  Prometheus  │─────►│   Grafana   │
└─────────────────┘  │      └──────────────┘      └─────────────┘
                     │             │
                     └─────────────┤
                                   │
                           ┌───────▼────────┐
                           │  Alertmanager  │
                           │  (Slack)       │
                           └────────────────┘
```

## 📦 Services

### Prometheus (`prometheus/`)
- **Port**: 9090
- **Config**: [prometheus.yml](prometheus/prometheus.yml)
- **Alert Rules**: [alert_rules.yml](prometheus/alert_rules.yml)
- **Scrapes**:
  - Prometheus (self-monitoring)
  - Node Exporter (system metrics)
  - App Demo (application metrics)

### Grafana
- **Port**: 3000
- Default credentials: `admin:admin`
- Data source: Prometheus

### Alertmanager (`alertmanager/`)
- **Port**: 9093
- **Config**: [alertmanager.yml](alertmanager/alertmanager.yml)
- Routes alerts to Slack notifications

### Node Exporter
- **Port**: 9100
- Collects system-level metrics (CPU, memory, disk, etc.)

### App Demo (`app-metrics-demo/`)
- **Port**: 8000
- **Language**: Python (Flask)
- **Metrics Endpoint**: `/metrics`
- **Home Endpoint**: `/` (increments request counter)

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose

### Running the Stack

```bash
docker-compose up -d
```

### Accessing Services
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000
- **Alertmanager**: http://localhost:9093
- **App Demo**: http://localhost:8000
- **App Metrics**: http://localhost:8000/metrics

## 📊 Monitoring Alerts

The stack includes the following alert rules ([alert_rules.yml](prometheus/alert_rules.yml)):

| Alert | Condition | Severity |
|-------|-----------|----------|
| **HighCPUUsage** | CPU > 80% for 1 minute | Warning |
| **HighMemoryUsage** | Memory > 85% | Critical |
| **NodeExporterDown** | Node Exporter unreachable for 30s | Critical |
| **AppDemoDown** | App Demo unreachable for 15s | Warning |

## 🔧 Configuration

### Slack Integration
To enable Slack notifications, update the webhook URL in [alertmanager/alertmanager.yml](alertmanager/alertmanager.yml):

```yaml
api_url: "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

## 📁 Project Structure

```
.
├── docker-compose.yml          # Service definitions
├── README.md                   # This file
├── prometheus/
│   ├── prometheus.yml          # Prometheus configuration
│   └── alert_rules.yml         # Alert rules
├── alertmanager/
│   └── alertmanager.yml        # Alertmanager configuration
└── app-metrics-demo/
    ├── app.py                  # Flask application with metrics
    ├── Dockerfile              # Docker image for app
    └── requirements.txt        # Python dependencies
```

## 🛑 Stopping the Stack

```bash
docker-compose down
```

## 📚 Resources

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Alertmanager Documentation](https://prometheus.io/docs/alerting/latest/alertmanager/)
- [Node Exporter Documentation](https://github.com/prometheus/node_exporter)
