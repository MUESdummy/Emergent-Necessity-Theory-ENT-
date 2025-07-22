# ENT Website Instructions

## Summary
I have successfully set up the Emergent Necessity Theory (ENT) repository to serve as a comprehensive wiki website at `emergent-necessity.org`. The implementation includes:

### Files Created:
- `index.html` - Main wiki homepage with complete ENT content
- `_config.yml` - Jekyll configuration for GitHub Pages
- `CNAME` - Custom domain configuration for emergent-necessity.org
- `404.html` - Custom 404 error page
- `.github/workflows/deploy.yml` - Automated deployment workflow
- `robots.txt` - SEO optimization
- `WEBSITE_README.md` - Website setup documentation

### Next Steps Required (Admin Access Needed):

1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Set Source to "Deploy from a branch"
   - Select branch: main / (root)
   - Enter custom domain: emergent-necessity.org
   - Enable "Enforce HTTPS"

2. **Configure DNS for emergent-necessity.org:**
   - Add CNAME record: `emergent-necessity.org` → `muesdummy.github.io`
   - Add CNAME record: `www.emergent-necessity.org` → `muesdummy.github.io`

3. **Verify SSL Certificate:**
   - GitHub will automatically provision SSL certificate for the custom domain
   - This may take a few minutes after DNS propagation

### Features Implemented:
- ✅ Complete ENT wiki content with all formulas and links
- ✅ Professional design matching ENT branding
- ✅ Direct links to all PDF papers and simulation files
- ✅ Integration with existing GitHub wiki
- ✅ Mobile-responsive design
- ✅ SEO optimization
- ✅ Automated deployment via GitHub Actions

The website will serve as the official ENT wiki at emergent-necessity.org once the domain configuration is completed.