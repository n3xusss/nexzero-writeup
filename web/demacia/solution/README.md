# Demacia Challenge

## Description

Welcome to the IDOR (Insecure Direct Object Reference) challenge! Your goal is to exploit IDOR vulnerabilities to access user profiles and files.

## Intended Approach

The challenge involves leveraging IDOR vulnerabilities to access unauthorized user profiles and files. Participants should carefully inspect the application's behavior, URL parameters, and authentication mechanisms.

## Flag

`nexus{This_is_so_ez_right}`

## Solution Write-up

### Step 1: Exploiting User Profiles

1. Visit the `/profile` endpoint with different `user_id` parameters to observe user profiles.
   - Example: http://localhost:3000/profile?user_id=1
2. Identify IDOR vulnerability conditions and exploit them to access profiles of other users.

### Step 2: Accessing Files

1. Explore the `/file` endpoint with different `file_id` and `owner_id` parameters.
   - Example: http://localhost:3000/file?file_id=1&owner_id=1
2. Look for conditions that allow access to files without proper authorization.
3. Exploit the vulnerability to access files, with special attention to the flag file (ID 3).

### Step 3: Retrieve the Flag

1. Once you have successfully exploited the vulnerabilities, find and retrieve the flag.
   - Example: http://localhost:3000/file?file_id=3&owner_id=3

## Notes

- Pay attention to the server logs for insights into authentication and user sessions.
- Keep in mind that IDOR vulnerabilities may involve manipulating URL parameters and exploiting authorization conditions.

## Author

Challenge created by Eve SatOrU.

## Resources

- medium: https://medium.com/@jetti.dinesh/insecure-direct-object-reference-idor-vulnerabilities-df551431eb7b

