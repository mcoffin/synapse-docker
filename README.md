# synapse-docker

[![Docker Pulls](https://img.shields.io/docker/pulls/mcoffin/synapse-docker.svg)](https://hub.docker.com/r/mcoffin/synapse-docker)

Docker container for running [synapse](https://github.com/airbnb/synapse).

This container runs the synpase process and using `supervisord` for process supervision.

# Why?

Synapse requires access to a way to restart haproxy instead of managing the process itself. `supervisord`, while usually an anti-pattern for docker containers, provides a nice interface atop unix sockets for `synapse` to access and restart `haproxy`.

# Overview

The `docker-entrypoint` script adds a couple of options to the synapse config file (`haproxy` restart command), renders it, and then starts `supervisord`, which manages both `synapse` and `haproxy`, and provides a way for `synapse` to restart `haproxy` via `supervisorctl`.

# Example usage

```
docker run --rm -v /path/to/some-synapse-config.yml:/synapse.yml mcoffin/synapse synapse /synapse.yml
```

An alternative usage would be to include the `synapse.yml` in it's own layer of a new image instead of as a volume. (This probably provides better performance on some docker backends).
