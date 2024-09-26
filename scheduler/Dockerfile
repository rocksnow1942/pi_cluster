FROM golang:1.23 AS builder

COPY . /src

WORKDIR /src

RUN GOOS=linux GOARCH=arm64 go build -o dist/scheduler .

FROM scratch

COPY --from=builder /src/dist/scheduler /

ENTRYPOINT ["/scheduler"]
