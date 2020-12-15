package aws

import (
	"os"
)

type (
	// Initialize filewalk channel
	fileWalk chan string

	// Route for s3 bucket
	Route struct {
		Bucket   string
		Category string
		Dir      string
	}

	// Context for templates
	Context struct {
		Name        string `json:"name"`
		Description string `json:"description"`
		Domain      string `json:"domain"`
		Phone       string `json:"phone"`
		Address     string `json:"address"`
		Email       string `json:"email"`
		Zip         []byte `json:"zip"`
	}
)

// Walk through folder
func (f fileWalk) Walk(path string, info os.FileInfo, err error) error {
	if err != nil {
		return err
	}

	if !info.IsDir() {
		f <- path
	}
	return nil
}