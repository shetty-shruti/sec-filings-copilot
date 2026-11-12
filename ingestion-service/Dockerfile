FROM golang:1.22 AS build
WORKDIR /src
COPY go.mod ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /out/poller ./cmd/poller

FROM gcr.io/distroless/static-debian12
COPY --from=build /out/poller /poller
ENTRYPOINT ["/poller"]
