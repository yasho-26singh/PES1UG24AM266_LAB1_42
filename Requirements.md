# Requirements Specification

## Internal Microservice Catalog & Health Portal

### Functional Requirements

| ID     | Type       | Description                                                                                                               | Priority | Acceptance Criteria                                                                                                                                                                | Rationale                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| FR-001 | Functional | The system shall ping each registered microservice health endpoint at 30-second intervals.                                | High     | **Pass:** Health probes are executed approximately every 30 seconds for all registered services. **Fail:** A registered service is not probed within 40 seconds.                   | Regular health probes are required to detect service failures quickly.                             |
| FR-002 | Functional | The system shall calculate and display the rolling 24-hour availability percentage for each microservice.                 | High     | **Pass:** Availability is calculated correctly from successful and failed health probes over the previous 24 hours. **Fail:** Incorrect or missing availability data is displayed. | Availability metrics help DevOps Engineers evaluate service reliability.                           |
| FR-003 | Functional | The system shall record and store the result of every health probe including timestamp, status, status code, and latency. | High     | **Pass:** Every probe record contains timestamp, status, status code, and latency. **Fail:** Any required probe information is missing or incomplete.                              | Historical probe data is required for availability calculations, troubleshooting and auditing.     |
| FR-004 | Functional | The system shall generate and dispatch an alert when a microservice fails three consecutive health probes.                | High     | **Pass:** An alert is generated and dispatched after the third consecutive failed probe. **Fail:** The alert is missing or generated before three consecutive failures.            | Consecutive failures indicate a potentially unavailable service and require operational attention. |
| FR-005 | Functional | The system shall provide searchable API documentation for all registered microservices.                                   | Medium   | **Pass:** API documentation can be searched and the documentation displayed is current. **Fail:** Documentation is missing, inaccessible or outdated.                              | Centralized API documentation helps developers understand and integrate with internal services.    |

---

## Non-Functional Requirements

| ID      | Type        | Description                                                                                                                                       | Priority | Acceptance Criteria                                                                                                                                                                                                                                   | Rationale                                                                                                   |
| ------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| NFR-001 | Performance | The service catalog dependency graph viewer shall render interactive node architectures containing up to 200 services smoothly.                   | High     | **Pass:** A dependency graph containing 200 services renders within 1 second and maintains at least 30 FPS during zoom and pan operations. **Fail:** Rendering takes more than 1 second or interaction falls below 30 FPS.                            | The portal must remain usable when visualizing large microservice architectures.                            |
| NFR-002 | Security    | The system shall protect service information and operational data through secure communication, authentication, authorization and access control. | High     | **Pass:** All traffic uses HTTPS, users are authenticated, and role-based access controls restrict unauthorized operations. **Fail:** Unauthenticated users can access protected information or unauthorized users can perform restricted operations. | Microservice information and operational health data may contain sensitive internal infrastructure details. |

---

## Requirement Summary

### Functional Requirements

* FR-001 – Periodic Health Probing
* FR-002 – Availability Calculation
* FR-003 – Health Probe Data Storage
* FR-004 – Failure Alert Generation
* FR-005 – API Documentation

### Non-Functional Requirements

* NFR-001 – Performance
* NFR-002 – Security
