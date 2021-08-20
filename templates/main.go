package main

import (
	"io/ioutil"
	"log"
	"net/http"
	"strings"
	"time"

	"github.com/myzhan/boomer"
)

func request() {

	url := Url
	method := Method
	Payload

	client := &http.Client{}
	req, err := http.NewRequest(method, url, Ipayload)

	ReqHeader
	start := time.Now()
	res, err := client.Do(req)
	if err != nil {
		log.Println(err)
		return
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	elapsed := time.Since(start)
	if strings.Contains(string(body), Assertstr)  {
		boomer.RecordSuccess(Type, Rname, elapsed.Nanoseconds()/int64(time.Millisecond), int64(10))
	} else {
		boomer.RecordFailure(Type, Rname, elapsed.Nanoseconds()/int64(time.Millisecond), string(body))
	}
}

func main() {
	task1 := &boomer.Task{
		Name: Rname,
		// The weight is used to distribute goroutines over multiple tasks.
		Weight: 1,
		Fn:     request,
	}

	boomer.Run(task1)
}