package main

import (
	"encoding/json"
	"fmt"
	awsevents "github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

type Response awsevents.APIGatewayProxyResponse

type AuthorizationRequest struct {
	ResponseType string `json:"response_type"`
	ClientID     string `json:"client_id"`
	RedirectURI  string `json:"redirect_uri"`
	Scope        string `json:"scope"`
	State        string `json:"state"`
}

func Handler(rawReq awsevents.APIGatewayProxyRequest) (Response, error) {
	out, _ := json.Marshal(rawReq)
	fmt.Println(string(out[:]))
	/*gov.MapData{
		"response_type": []string{"required"},
		"client_id":     []string{"required"},
		"redirect_uri":  []string{"required"},
	}*/

	/*
		Use the multi value option when retrieving data and ENSURE the length === 1. Otherwise,
		there is a high chance something was wrong, and should throw an error.

		Flatten data for validation? Introduces security flaw of allowing data to be sent from alternative
			locations?
		Not if you just take the data from the proper locations to start...?
		Then you are just doubling the work and creating an extra struct for everything you need.
	*/

	/*fmt.Println("HEADERS")
	fmt.Println(rawReq.Headers)
	// USE
	fmt.Println("MultiValueHeaders")
	fmt.Println(rawReq.MultiValueHeaders)
	fmt.Println("QueryStringParameters")
	fmt.Println(rawReq.QueryStringParameters)
	// USE
	fmt.Println("MultiValueQueryStringParameters")
	fmt.Println(rawReq.MultiValueQueryStringParameters)
	fmt.Println("PathParameters")
	fmt.Println(rawReq.PathParameters)
	fmt.Println("StageVariables")
	fmt.Println(rawReq.StageVariables)
	fmt.Println("RequestContext")
	fmt.Println(rawReq.RequestContext)
	// USE
	fmt.Println("Body")
	fmt.Println(rawReq.Body)
	fmt.Println(rawReq.Body)*/

	return Response{
		StatusCode: 200,
		Body:       string(out[:]),
	}, nil
}

func main() {
	lambda.Start(Handler)
}
