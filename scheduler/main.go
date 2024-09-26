package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Received request from", r.RemoteAddr)
		fmt.Fprint(w, "Hello, World!\n")
	})
	fmt.Println("Starting server on port 80")
	http.ListenAndServe(":80", nil)
}
