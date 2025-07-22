# DNS Setup for Custom Domain

## Step 1: Create CNAME file
This repository needs a `CNAME` file containing your custom domain name.

**Example CNAME file content:**
```
yourdomain.com
```
OR
```
www.yourdomain.com
```

## Step 2: DNS Configuration at your Domain Registrar

### Option A: Using CNAME Record (Recommended for www subdomain)
If your domain is `www.yourdomain.com`:
```
Type: CNAME
Name: www
Value: muesdummy.github.io
TTL: 3600 (or default)
```

### Option B: Using A Records (For apex domain like yourdomain.com)
If your domain is `yourdomain.com` (no www):
```
Type: A
Name: @ (or leave blank)
Value: 185.199.108.153
TTL: 3600

Type: A  
Name: @ (or leave blank)
Value: 185.199.109.153
TTL: 3600

Type: A
Name: @ (or leave blank) 
Value: 185.199.110.153
TTL: 3600

Type: A
Name: @ (or leave blank)
Value: 185.199.111.153
TTL: 3600
```

## Step 3: Enable GitHub Pages
1. Go to your repository settings
2. Scroll down to "Pages" section
3. Set Source to "Deploy from a branch"
4. Select "main" branch
5. Select "/ (root)" folder
6. Click Save

## Step 4: Add Custom Domain in GitHub
1. In the same Pages settings
2. Under "Custom domain", enter your domain
3. Check "Enforce HTTPS" 
4. GitHub will automatically create the CNAME file

## Step 5: Verify Setup
- DNS changes can take up to 24-48 hours to propagate
- You can check DNS propagation at: https://dnschecker.org
- GitHub will verify your domain and issue SSL certificate

## Common Issues
- **404 Error**: Check that `index.html` exists in root directory
- **DNS Not Resolving**: Wait for propagation or check DNS records
- **Certificate Issues**: Ensure "Enforce HTTPS" is enabled and wait for automatic certificate

## What Domain Did You Purchase?
Please update the `CNAME` file with your actual domain name.