# synapse-docker

Docker container for running [synapse](https://github.com/airbnb/synapse).

This container runs the synpase process and using `supervisord` for process supervision.

# Example usage

```
docker run --rm -v /path/to/some-synapse-config.yml:/synapse.yml mcoffin/synapse synapse /synapse.yml
```
