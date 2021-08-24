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

	url := "https://open-pre.shiguangkey.com/api/udb/cfg/areacode/refresh?pageIndex=1&pageSize=2"
	method := "POST"
	payload := strings.NewReader("1111=2222&3333=4444")

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	req.Header.Add("User-Agent","Mozilla/5.0 Lemon Little Girl")
    req.Header.Add("Content-Type","application/json")
    req.Header.Add("Accept","application/json")
    req.Header.Add("Authorization","JWT $token")
    
	start := time.Now()
	res, err := client.Do(req)
	if err != nil {
		log.Println(err)
		return
	}

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	elapsed := time.Since(start)
	if strings.Contains(string(body), "do123")  {
		boomer.RecordSuccess("Https", "创建项目接口_正向用例", elapsed.Nanoseconds()/int64(time.Millisecond), int64(10))
	} else {
		boomer.RecordFailure("Https", "创建项目接口_正向用例", elapsed.Nanoseconds()/int64(time.Millisecond), string(body))
	}
}

func main() {
	task1 := &boomer.Task{
		Name: "创建项目接口_正向用例",
		// The weight is used to distribute goroutines over multiple tasks.
		Weight: 1,
		Fn:     request,
	}

	boomer.Run(task1)
}