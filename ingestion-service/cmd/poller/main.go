// Command poller checks SEC EDGAR on a schedule for new 10-K filings and
// publishes a filings.new event to Kafka for each one (weeks 5 to 6).
package main

import (
	"log"
	"os"
)

func main() {
	ua := os.Getenv("SEC_USER_AGENT")
	if ua == "" {
		log.Fatal("SEC_USER_AGENT is required (\"Name email\")")
	}
	log.Println("poller: not implemented yet (weeks 5 to 6)")
}
