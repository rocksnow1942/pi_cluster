package main

import (
	"fmt"
	"log"
	"net"
	"net/http"
)

type Counter[T comparable] = map[T]int64

func Inc[T comparable](c Counter[T], key T) {
	c[key]++
}

func main() {
	var s Counter[string] = make(Counter[string])
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Received request from", r.RemoteAddr)
		// echo back the reqeust url count
		Inc(s, r.URL.Path)
		fmt.Fprintf(w, "Hello, you are the %dth visitor to %s!\n", s[r.URL.Path], r.URL.Path)
	})
	fmt.Println("Started server on port 80!!")
	http.ListenAndServe(":80", nil)
}

func handleHello() {
	con, err := net.Dial("tcp", "192.168.86.1")
	con.Close()
	fmt.Printf("closed, %v", con)
	if err != nil {
		log.Fatalf("fatal %v", err)
	}
}
