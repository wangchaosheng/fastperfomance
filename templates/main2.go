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

	url := "https://ntcapi-pre.shiguangkey.com/api/marketing/goods/pc/quality?num=10?num=10&mom=1"
	method := "get"
	payload := strings.NewReader("c=1")

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	req.Header.Add("header","header2")
    
	start := time.Now()
	res, err := client.Do(req)
	if err != nil {
		log.Println(err)
		return
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	elapsed := time.Since(start)
	if strings.Contains(string(body), "success")  {
		boomer.RecordSuccess("Https", "首页获取商品", elapsed.Nanoseconds()/int64(time.Millisecond), int64(10))
	} else {
		boomer.RecordFailure("Https", "首页获取商品", elapsed.Nanoseconds()/int64(time.Millisecond), string(body))
	}
}

func main() {
	task1 := &boomer.Task{
		Name: "首页获取商品",
		// The weight is used to distribute goroutines over multiple tasks.
		Weight: 1,
		Fn:     request,
	}

	boomer.Run(task1)
}