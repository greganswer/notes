# Checklist

## Database

- [ ] Develope a Multi-tenant data model
- [ ] Index frequently queried columns
- [ ] Add foreign key constraints

## Backend

- [ ] Automated acceptance and unit tests
- [ ] Error and info logging to `stdout`
- [ ] Error notifications (email, Slack, etc.)
- [ ] Health checks endpoint
- [ ] Require Access Token for all routes
- [ ] Request Throttling
- [ ] Use [Auth0](https://auth0.com/) for authentication
- [ ] Use [Stripe](https://stripe.com/fr) for online payments
- [ ] Maintain internal and external API documentation
- [ ] Decide on a caching strategy
- [ ] Continuous Integration

## Devops

- [ ] Simplified 1 line deployment command
- [ ] Continuous Delivery/Deployment
- [ ] Require SSL
- [ ] Hourly Database backups
- [ ] Load balancing
- [ ] Auto-scaling
- [ ] Error logging 
- [ ] Service replication (3 or more)
- [ ] Use Docker containers (or something similar)
- [ ] Use a container management system like ECS/EKS in AWS or Kubernetes engine in GCP
- [ ] Use Elastic Beanstalk or App Engine for auto-scaling and load-balancing
- [ ] Deploy to multiple availability zones (based on user locations)
- [ ] Host static web files and serve them via Content Delivery Network (CDN)
- [ ] Decide on a caching strategy

## References

1. [Distributed Systems (Medium article)](https://medium.freecodecamp.org/distributed-systems-when-you-should-build-them-and-how-to-scale-a-step-by-step-guide-37e76a177218)