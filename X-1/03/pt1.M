% Read all images in a folder
files = dir('*.jpg');
num_images = length(files);

% Create a montage of all images
montage_image = zeros(size(imread(files(1).name),1),num_images);
for i=1:num_images
    image = imread(files(i).name);
    montage_image(:,i) = image(:);
end

% Plot the montage image
imshow(montage_image);
