.PHONY: build
build:
# podman build --platform linux/amd64,linux/arm64 -t scheduler .
	podman build --jobs=2 --platform linux/amd64,linux/arm64 --manifest localhost/scheduler-mp .

.PHONY: push
push:
	@gcloud auth print-access-token --quiet | podman login -u oauth2accesstoken --password-stdin https://us-docker.pkg.dev
	@podman tag localhost/scheduler-mp us-docker.pkg.dev/hui-dev-399904/pi-cluster/scheduler-mp
	@podman manifest rm localhost/scheduler-mp
	@podman manifest push us-docker.pkg.dev/hui-dev-399904/pi-cluster/scheduler-mp

.PHONY: prune
prune:
	podman image prune -f
