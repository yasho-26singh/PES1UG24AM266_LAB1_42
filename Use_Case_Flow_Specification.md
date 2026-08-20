# Use-Case Flow Specification

## UC-001 – Monitor Service Health

### Use Case Information

| Field             | Details                                                    |
| ----------------- | ---------------------------------------------------------- |
| **Use Case ID**   | UC-001                                                     |
| **Use Case Name** | Monitor Service Health                                     |
| **Primary Actor** | DevOps Engineer                                            |
| **Goal**          | Monitor microservice health and availability in real time. |

---

## 1. Preconditions

1. The user is authenticated and has permission to access the portal.
2. At least one microservice is registered in the system.
3. The microservice health endpoints are configured and accessible.

---

## 2. Main Success Scenario

1. The DevOps Engineer navigates to **Monitor Service Health**.
2. The system displays all registered microservices with their current health status.
3. The system sends a health probe to each microservice every 30 seconds.
4. Each microservice returns a health response.
5. The system records the response timestamp, status, status code and latency.
6. The system calculates the rolling 24-hour availability percentage.
7. The system updates the health monitoring dashboard.
8. The DevOps Engineer views the current health and availability information.
9. The use case ends successfully.

---

## 3. Alternate Flow – Service Failure

**Trigger:** A microservice fails three consecutive health probes.

**A1.** The system detects that a microservice has failed a health probe.

**A2.** The system records the failed probe.

**A3.** The system checks whether three consecutive probes have failed.

**A4.** If fewer than three consecutive failures have occurred, the system continues normal monitoring.

**A5.** If three consecutive failures have occurred, the system generates a failure alert.

**A6.** The system sends the alert through the configured Notification Service.

**A7.** The alert is recorded and displayed under **Manage Alerts**.

**A8.** The system returns to the main monitoring flow.

---

## 4. Postconditions

1. The latest health status of all monitored microservices is stored.
2. Probe results and availability information are updated.
3. Any qualifying service failure is recorded as an alert.
4. The monitoring dashboard reflects the latest service status.

---

## 5. Success Guarantee

The system continuously monitors registered microservices and provides accurate health and availability information to authorized users.
