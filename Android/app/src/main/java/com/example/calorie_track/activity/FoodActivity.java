package com.example.calorie_track.activity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.example.calorie_track.R;

public class FoodActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_food);

        ImageView imageView=findViewById(R.id.foodImage);
        String imagePath = getIntent().getStringExtra("imagePath");
        if (imagePath != null) {
            Bitmap bitmap = BitmapFactory.decodeFile(imagePath);
            imageView.getLayoutParams().width = 800; // Width in pixels
            imageView.getLayoutParams().height = 800; // Height in pixels
            imageView.requestLayout();
            imageView.setImageBitmap(bitmap);
        }
        Button button=findViewById(R.id.home);
        button.setOnClickListener(v -> backToHome());
    }

    private void backToHome(){
        Intent intent = new Intent(FoodActivity.this, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        startActivity(intent);
        finish();
    }
}