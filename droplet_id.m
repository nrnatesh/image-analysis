
droplets = imread('/home/nrnatesh/shenlab/Droplet-organoid/image-analysis/input_images/T2.tif');
% imshow(rgb);
%[centers,radii] = imfindcircles(rgb,[45 60],'Sensitivity',1, 'EdgeThreshold',.7)

%h = viscircles(centers,radii);

figure (1)
imshow(droplets);
coord_data = readtable('/home/nrnatesh/shenlab/Droplet-organoid/image-analysis/coordinates.csv');
coord_array = table2array(coord_data);



for i = 1:length(coord_array)
circle(i) = drawcircle('Center',[coord_array(i,1),coord_array(i,2)],'Radius',coord_array(i,3));
mask = createMask(circle(i));
end

