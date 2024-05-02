package main

import (
	"flag"
	"fmt"
	"net/http"
	"sync"
	"time"
)

func main() {
	// Definindo a flag para o número de requisições simultâneas
	numRequests := flag.Int("n", 4, "number of simultaneous requests")
	flag.Parse()

	// Endpoints para teste
	endpoints := []string{"http://localhost:3000/tasks", "http://localhost:3001/tasks"}

	// Primeiro teste: requisições sequenciais para cada endpoint
	fmt.Println("Iniciando o primeiro teste")
	for _, endpoint := range endpoints {
		now := time.Now()
		makeRequest(endpoint)
		duration := time.Since(now)
		fmt.Printf("Total time for one request to %s: %s\n", endpoint, duration)
	}

	// Espera de 1 segundo entre os testes
	time.Sleep(1 * time.Second)

	// Segundo teste: requisições simultâneas para cada endpoint
	fmt.Println("Iniciando o segundo teste")
	var wg sync.WaitGroup
	for _, endpoint := range endpoints {
		wg.Add(1)
		go func(ep string) {
			defer wg.Done()
			makeMultipleSimultaneousRequests(ep, *numRequests)
		}(endpoint)
	}
	wg.Wait()
}

// makeRequest envia uma requisição GET ao endpoint especificado
func makeRequest(endpoint string) {
	req, err := http.NewRequest("GET", endpoint, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}
	req.Header.Add("Authorization", "03fd5486-2030-47cf-bf14-0e569d64fad9")
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return
	}
	defer resp.Body.Close()
}

// makeMultipleSimultaneousRequests realiza um número definido de requisições simultâneas ao mesmo endpoint
func makeMultipleSimultaneousRequests(endpoint string, count int) {
	var wg sync.WaitGroup
	startTime := time.Now()

	for i := 0; i < count; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			makeRequest(endpoint)
		}()
	}
	wg.Wait()

	totalTime := time.Since(startTime)
	fmt.Printf("Total time for %d simultaneous requests to %s: %s\n", count, endpoint, totalTime)
}
