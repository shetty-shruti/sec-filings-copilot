// Package edgar is a rate-limited (under 10 req/s) client for data.sec.gov.
package edgar

// Filing is one 10-K found in a company's submissions feed.
type Filing struct {
	Ticker          string
	CIK             int
	AccessionNumber string
	FiscalYear      int
	FilingDate      string
	URL             string
}
