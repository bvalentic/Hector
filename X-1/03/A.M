% Read all images in a folder
files = dir('*.jpg');
num_images = length(files);

% Get the maximum height and width of all images
max_height = 0;
max_width = 0;
for i = 1:num_images
    image = imread(files(i).name);
    [height, width, ~] = size(image);
    max_height = max(max_height, height);
    max_width = max(max_width, width);
end

% Create a montage of all images with consistent dimensions
montage_image = zeros(max_height, max_width * num_images, 3, 'uint8'); % 3 for RGB
for i = 1:num_images
    image = imread(files(i).name);
    [height, width, ~] = size(image);
    montage_image(1:height, (i-1)*max_width+1:i*max_width, :) = image;
end

% Plot the montage image
imshow(montage_image);
