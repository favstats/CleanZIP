use std::io::{Cursor, Read, Write};
use wasm_bindgen::prelude::*;
use zip::{write::FileOptions, ZipArchive, ZipWriter};

#[wasm_bindgen]
pub fn filter_zip(data: &[u8]) -> Result<Vec<u8>, JsValue> {
    let reader = Cursor::new(data);
    let mut zip = ZipArchive::new(reader).map_err(|e| JsValue::from_str(&format!("Error reading zip: {}", e)))?;
    let mut new_zip_data = vec![];

    {
        // Create a new scope for new_zip to ensure it is dropped before returning new_zip_data
        let mut new_zip = ZipWriter::new(Cursor::new(&mut new_zip_data));
        let options = FileOptions::default().compression_method(zip::CompressionMethod::Deflated);

        for i in 0..zip.len() {
            let mut file = zip.by_index(i).map_err(|e| JsValue::from_str(&format!("Error reading zip entry: {}", e)))?;
            let file_name = file.name().to_string();

            if file_name.ends_with(".json") || file_name.ends_with(".csv") || file_name.ends_with(".html") {
                let mut buffer = vec![];
                file.read_to_end(&mut buffer).map_err(|e| JsValue::from_str(&format!("Error reading file: {}", e)))?;
                new_zip.start_file(file_name, options).map_err(|e| JsValue::from_str(&format!("Error writing file: {}", e)))?;
                new_zip.write_all(&buffer).map_err(|e| JsValue::from_str(&format!("Error writing file data: {}", e)))?;
            }
        }

        new_zip.finish().map_err(|e| JsValue::from_str(&format!("Error finishing zip: {}", e)))?;
    } // new_zip goes out of scope and is dropped here

    Ok(new_zip_data)
}
