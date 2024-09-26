# Description: Dockerfile for building the scheduler binary
FROM --platform=$BUILDPLATFORM golang:1.23 AS builder
ARG TARGETOS
ARG TARGETARCH
ARG BUILDPLATFORM
ARG TARGETPLATFORM
COPY . /src

WORKDIR /src

# create a build based on `--platform=$BUILDPLATFORM` argument
RUN echo "BUILDPLATFORM=${BUILDPLATFORM}, TARGETPLATFORM=${TARGETPLATFORM}"
RUN echo "TARGETOS=${TARGETOS}, TARGETARCH=${TARGETARCH}"
RUN GOOS=${TARGETOS} GOARCH=${TARGETARCH} go build -o dist/scheduler .

FROM scratch
COPY --from=builder /src/dist/scheduler /
ENTRYPOINT ["/scheduler"]
