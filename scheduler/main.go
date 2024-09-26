package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Received request from", r.RemoteAddr)
		// echo back the reqeust url
		fmt.Fprint(w, "Hello, World!\nFrom:"+r.URL.Path)
	})
	fmt.Println("Started server on port 80!!")
	http.ListenAndServe(":80", nil)
}
