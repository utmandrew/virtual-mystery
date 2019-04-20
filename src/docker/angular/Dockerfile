## Stage 2: Angular Deployment ##
FROM httpd:2.4

# Copy angular production build files
COPY vm-angular/dist/vm-angular /usr/local/apache2/htdocs
# Uncomment when using multistage build with Dockerfile.build
# COPY --from=builder /opt/dist/vm-angular/* /var/www/html

# Copy apache .htaccess files
COPY docker/angular/.htaccess /usr/local/apache2/htdocs

# Copy apache config files 
COPY docker/angular/httpd.conf /usr/local/apache2/conf




