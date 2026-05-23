# Container Usage

This container image is intended for **on-demand CLI runs** (jobs or scheduled tasks).  
If you need a hosted API, wrap the CLI in a service layer and expose your own endpoints.

---

## Build locally

```bash
docker build -t user-scanner:local .
```

## Run a single scan

```bash
docker run --rm user-scanner:local -u johndoe
```

## Use input/output files

Mount a local directory into the container and reference paths under `/data`.

```bash
docker run --rm -v "$PWD":/data \
  user-scanner:local \
  -uf /data/usernames.txt \
  -o /data/report.json \
  -f json
```

## Use a proxy list

```bash
docker run --rm -v "$PWD":/data \
  user-scanner:local \
  -u johndoe \
  -P /data/proxies.txt \
  --validate-proxies
```

---

## Publish to a registry (GHCR example)

```bash
docker tag user-scanner:local ghcr.io/<org>/user-scanner:1.3.6.6
docker push ghcr.io/<org>/user-scanner:1.3.6.6
```

---

## Kubernetes job example

See [`deploy/kubernetes-job.yaml`](../deploy/kubernetes-job.yaml) for a minimal Job manifest.  
Update the `image:` and `args:` fields to match your target and scan.
