# ENT Website Setup

This repository serves the official website for Emergent Necessity Theory (ENT) at https://emergent-necessity.org

## Website Structure

- `index.html` - Main wiki homepage
- `_config.yml` - Jekyll configuration for GitHub Pages
- `CNAME` - Custom domain configuration
- `404.html` - Custom 404 error page
- `.github/workflows/deploy.yml` - GitHub Actions deployment workflow
- `robots.txt` - Search engine instructions

## Custom Domain Setup

The website is configured to serve from the custom domain `emergent-necessity.org`. 

To complete the setup:

1. Configure DNS for emergent-necessity.org to point to GitHub Pages:
   - Add CNAME record: `emergent-necessity.org` → `muesdummy.github.io`
   - Add CNAME record: `www.emergent-necessity.org` → `muesdummy.github.io`

2. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)
   - Custom domain: emergent-necessity.org

3. Enable HTTPS enforcement in GitHub Pages settings

## Content

The website serves as a comprehensive wiki for ENT, featuring:

- Theory overview and core equations
- Simulation results and data
- Links to papers and resources
- Quick navigation to GitHub wiki
- Direct access to PDF documents and code

## Development

The site uses static HTML with embedded CSS for fast loading and broad compatibility. All ENT resources in the repository are directly accessible via the website.