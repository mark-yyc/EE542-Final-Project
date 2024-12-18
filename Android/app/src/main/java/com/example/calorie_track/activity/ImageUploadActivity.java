package com.example.calorie_track.activity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.calorie_track.R;
import com.example.calorie_track.data.CalorieInfo;
import com.example.calorie_track.service.CalorieService;
import com.example.calorie_track.util.RetrofitClient;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class ImageUploadActivity extends AppCompatActivity {

    private static final int PICK_IMAGE_REQUEST = 1;
    private Button buttonSelect;

    private Button buttonUpload;

    private ImageView imageView;

    private Bitmap bitmap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.settings_activity);

        buttonSelect = findViewById(R.id.buttonSelect);
        buttonUpload= findViewById(R.id.buttonUpload);

        imageView = findViewById(R.id.imageView);

        buttonSelect.setOnClickListener(v -> openFileChooser());
        buttonUpload.setOnClickListener(v -> uploadImage());
    }

    private void openFileChooser() {
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_IMAGE_REQUEST);
    }

    private void uploadImage(){
        CalorieService calorieService = RetrofitClient.getInstance().create(CalorieService.class);

        Call<CalorieInfo> call = calorieService.uploadImage();
        call.enqueue(new Callback<CalorieInfo>() {
            @Override
            public void onResponse(Call<CalorieInfo> call, Response<CalorieInfo> response) {
                if (response.isSuccessful() && response.body() != null) {
                    CalorieInfo data = response.body();
                    Log.d("API_RESPONSE", data.toString());
                } else {
                    Log.e("API_ERROR", "Response unsuccessful or empty");
                }
            }

            @Override
            public void onFailure(Call<CalorieInfo> call, Throwable t) {
                Log.e("API_ERROR", "Failed to fetch data", t);
            }
        });

        File cacheDir = getCacheDir();
        File tempFile = new File(cacheDir, "temp_image.png");

        try (FileOutputStream fos = new FileOutputStream(tempFile)) {
            bitmap.compress(Bitmap.CompressFormat.PNG, 100, fos);
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            Intent intent = new Intent(ImageUploadActivity.this, FoodActivity.class);
            intent.putExtra("imagePath", tempFile.getAbsolutePath()); // Pass the file path
            startActivity(intent);
        } catch (Exception e) {
            e.printStackTrace();
            // Show error info as a Toast
            Toast.makeText(this, "Error: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_IMAGE_REQUEST && resultCode == RESULT_OK && data != null && data.getData() != null) {
            Uri imageUri = data.getData();

            try {
                bitmap = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imageUri);

                // Set fixed size programmatically
                imageView.getLayoutParams().width = 800; // Width in pixels
                imageView.getLayoutParams().height = 800; // Height in pixels
                imageView.requestLayout();

                // Display the image
                imageView.setImageBitmap(bitmap);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}