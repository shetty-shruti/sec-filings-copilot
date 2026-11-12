// Package publisher sends filing events to Kafka (or Azure Event Hubs via its Kafka endpoint).
package publisher

// FilingNewEvent is the payload on the filings.new topic. AccessionNumber is the idempotency key.
type FilingNewEvent struct {
	Ticker          string `json:"ticker"`
	CIK             int    `json:"cik"`
	AccessionNumber string `json:"accession_number"`
	FiscalYear      int    `json:"fiscal_year"`
	StoragePath     string `json:"storage_path"`
	SourceURL       string `json:"source_url"`
}
