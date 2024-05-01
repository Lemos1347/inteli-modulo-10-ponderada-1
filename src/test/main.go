package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

func main() {
	// Endpoints para teste
	endpoints := []string{"http://localhost:3000/tasks", "http://localhost:3001/tasks"}

	// Primeiro teste: requisições sequenciais para cada endpoint
	fmt.Println("Iniciando o primeiro teste")
	for _, endpoint := range endpoints {
		makeRequest(endpoint)
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
			makeFourSimultaneousRequests(ep)
		}(endpoint)
	}
	wg.Wait()
}

// makeRequest envia uma requisição GET ao endpoint especificado e imprime o tempo de envio
func makeRequest(endpoint string) {
	req, err := http.NewRequest("GET", endpoint, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}
	req.Header.Add("Authorization", "03fd5486-2030-47cf-bf14-0e569d64fad9")
	client := &http.Client{}
	requestTime := time.Now()
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()
	fmt.Printf("Request sent to %s at: %s\n", endpoint, requestTime.Format("2006-01-02 15:04:05"))
}

// makeFourSimultaneousRequests realiza quatro requisições simultâneas ao mesmo endpoint
func makeFourSimultaneousRequests(endpoint string) {
	var wg sync.WaitGroup
	startTime := time.Now()

	for i := 0; i < 4; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			makeRequest(endpoint)
		}()
	}
	wg.Wait()

	totalTime := time.Since(startTime)
	fmt.Printf("Total time for four simultaneous requests to %s: %s\n", endpoint, totalTime)
}
