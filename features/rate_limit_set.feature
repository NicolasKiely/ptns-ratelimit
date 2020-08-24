Scenario: Set rate limit of domain
Given an adminstrative command line user
When the user sets the rate for a domain www.example.com to 50
Then the rate limit for the domain www.example.com should be 50
