import bpy
import os

def configure_and_render(output_path="//renders/tour_walkthrough.mp4", preview=False):
    scene = bpy.context.scene
    
    # 1. Output Format & Codec
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.ffmpeg.constant_rate_factor = "HIGH"
    scene.render.ffmpeg.ffmpeg_preset = "GOOD"
    scene.render.filepath = output_path
    
    # 2. Engine Selection (EEVEE for instant preview, Cycles for photorealism)
    if preview:
        scene.render.engine = "BLENDER_EEVEE_NEXT" if hasattr(bpy.types, "RenderSettings") else "BLENDER_EEVEE"
        scene.eevee.use_gtao = True
        scene.eevee.use_bloom = True
        scene.render.resolution_percentage = 50  # Fast 720p draft
    else:
        scene.render.engine = "CYCLES"
        scene.cycles.device = "GPU"
        scene.cycles.samples = 128
        scene.cycles.use_denoising = True
        scene.render.resolution_x = 1920
        scene.render.resolution_y = 1080
        scene.render.resolution_percentage = 100

    # 3. Trigger Render Animation
    bpy.ops.render.render(animation=True)

if __name__ == "__main__":
    configure_and_render()